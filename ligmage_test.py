import filetype
import logging
import pathlib
import time
import open_clip
import torch
from PIL import Image


def ligmage(chemin, seuil_temp, mots):
    logging.info("Thread ligmage: starting.")
    start_time = time.time()

    # test avec optimum
    # onnx_path = "models/"
    # model = ORTModelForImageClassification.from_pretrained(onnx_path, file_name="clip-image-int8.ort")
    # tokenizer = AutoTokenizer.from_pretrained(onnx_path)
    #
    # q8_clf = pipeline("image-classification", model=model, tokenizer=tokenizer)
    #
    # q8_clf("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
    # # q8_clf("What is the exchange rate like on this app?")
    #
    # input()

    # fin test

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k', device=device)
    tokenizer = open_clip.get_tokenizer('ViT-B-32')

    images = []
    hash_table = {}

    dossier = pathlib.Path(chemin)
    for fichier in dossier.iterdir():
        if fichier.is_file() and filetype.is_image(fichier):
            images.append(fichier)

    for image in images:
        imagent = preprocess(Image.open(image)).unsqueeze(0).to(device)
        text = tokenizer(mots).to(device)
        with torch.no_grad():
            image_features = model.encode_image(imagent)
            text_features = model.encode_text(text)

            # model(imagent, text)
            cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
            probs = cos(image_features, text_features)

            nom_fichier = image.name  # Fonction à définir pour obtenir le nom du fichier

            hash_table[nom_fichier] = probs[0].item()

    hash_table = dict(sorted(hash_table.items(), key=lambda item: item[1], reverse=True))

    # print les fichiers par ordre de préférence suivant la recherche
    print(hash_table)
    # print(sorted(hash_table, key=hash_table.get, reverse=True))

    end_time = time.time()
    print("Temps total : {:.2f} secondes".format(end_time - start_time))
    logging.info("Thread ligmage: finishing.")


if __name__ == "__main__":
    ligmage('/home/rizsane/Pictures/Rigolo/Tusky/', 0.2, ["bourgeoisie"])
