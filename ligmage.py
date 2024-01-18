from collections import OrderedDict

import filetype
import logging
import pathlib
import time
import open_clip
import torch
from PIL import Image
from PySide6.QtCore import Property, QObject, Signal


class Ligmage(QObject):
    progress_changed = Signal(str)
    images_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self._progress = [0, 0]
        self._images = ["", "", ""]
        self.chemin = ""
        self.recursive = True

        self.device = None
        self.model, self.preprocess = None, None
        self.tokenizer = None

        self.files = OrderedDict()

    @Property(list)
    def progress(self):
        return self._progress

    @Property(list)
    def images(self):
        return self._images

    def load_model(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, _, self.preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k', device=self.device)
        self.tokenizer = open_clip.get_tokenizer('ViT-B-32')

    def set_chemin(self, chemin, recursive):
        self.chemin = chemin
        self.recursive = recursive

    def ligmage(self, recherche):
        logging.info("Thread ligmage: starting.")

        if self.model is None:
            logging.info("Thread ligmage: loading model.")
            self.load_model()
            logging.info("Thread ligmage: model loaded.")

        mots = recherche.split()
        start_time = time.time()

        print(mots)
        print(self.chemin)

        images = []
        hash_table = {}

        dossier = pathlib.Path(self.chemin)
        if self.recursive:
            for fichier in dossier.rglob("*"):
                if fichier.is_file() and filetype.is_image(fichier):
                    images.append(fichier)
        else:
            for fichier in dossier.iterdir():
                if fichier.is_file() and filetype.is_image(fichier):
                    images.append(fichier)

        self._progress = [0, len(images)]
        self.progress_changed.emit(f"{0}/{len(images)}")
        self.images_changed.emit(f"")

        for image in images:
            imagent = self.preprocess(Image.open(image)).unsqueeze(0).to(self.device)
            text = self.tokenizer(mots).to(self.device)
            with torch.no_grad():
                image_features = self.model.encode_image(imagent)
                text_features = self.model.encode_text(text)

                # model(imagent, text)
                cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
                probs = cos(image_features, text_features)

                nom_fichier = image.as_uri()  # Fonction à définir pour obtenir le nom du fichier

                hash_table[nom_fichier] = probs[0].item()

                hash_table = dict(sorted(hash_table.items(), key=lambda item: item[1], reverse=True))

                self._progress[0] += 1
                self.progress_changed.emit(f"{self._progress[0]}/{len(images)}")

                best_keys = list(hash_table.keys())[:3]
                self._images = best_keys
                best_keys_str = ','.join(best_keys)
                self.images_changed.emit(best_keys_str)

                if probs[0].item() > 0.10:
                    self.files[nom_fichier] = probs[0].item()
                    self.files = dict(sorted(self.files.items(), key=lambda item: item[1], reverse=True))
                    # print(self.files.keys())

        hash_table = dict(sorted(hash_table.items(), key=lambda item: item[1], reverse=True))

        # print les fichiers par ordre de préférence suivant la recherche
        print(hash_table)
        # print(sorted(hash_table, key=hash_table.get, reverse=True))

        end_time = time.time()
        print("Temps total : {:.2f} secondes".format(end_time - start_time))
        logging.info("Thread ligmage: finishing.")
