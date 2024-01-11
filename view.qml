import QtCore
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts
import QtQuick.Dialogs
import Qt.labs.platform

Window {
    width: 720
    height: 480
    visible: true
    title: "Ligmage"

    FolderDialog {
        id: folderDialog
        title: qsTr("Dossier d'images")
        currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
        onAccepted: {
            pathText.text = "Dossier choisi : " + folder
            backend.file_url = folder
        }
    }

    function copyImageToClipboard(image) {
        if (image.status === Image.Ready) {
            /*const clipboard = Qt.clipboard;
            clipboard.image = image.source;*/

            backend.copy_image(image.source.toString());
        }
    }

    RowLayout {
        anchors.fill: parent

        ColumnLayout {
            Layout.margins: 10
            Layout.fillHeight: true
            Layout.alignment: Qt.AlignTop | Qt.AlignHCenter
            

            // --
            RowLayout {
                Button {
                    id: chooseImageButton
                    objectName: "chooseImageButton"
                    text: qsTr("Choisir le dossier")
                    onClicked: folderDialog.visible = true
                }

                Text {
                    id: pathText/*
                    width: parent.width
                    wrapMode: Text.Wrap
                    elide: Text.ElideRight*/
                    text: "Dossier"
                }
            }

            RowLayout {
                TextInput {
                    id: searchInput
                    text: "cat"
                }

                Button {
                    id: ligmageButton
                    objectName: "ligmageButton"
                    text: qsTr("Chercher")
                    onClicked: backend.run_ligmage(searchInput.text)
                }
            }

            Text {
                id: progressText
                text: "Statut : 0/0"
                font.pointSize: 12
                color: "green"

                Component.onCompleted: {
                    ligmage.progress_changed.connect(updateProgressText)
                }

                function updateProgressText() {
                    progressText.text = "Statut : " + ligmage.progress.join("/")
                }
            }

            Text {
                id: matchingImagesText
                text: "les 3 images correspondant le plus sont : "
                font.pointSize: 12
                color: "red"

                Component.onCompleted: {
                    ligmage.images_changed.connect(updateProgressText)
                }

                function updateProgressText() {
                    matchingImagesText.text = "les 3 images correspondant le plus sont : " + ligmage.images.join("\n")
                    img1.source = folderDialog.folder + "/" + ligmage.images[0];
                    img2.source = folderDialog.folder + "/" + ligmage.images[1];
                    img3.source = folderDialog.folder + "/" + ligmage.images[2];

                    img1Text.text = ligmage.images[0];
                    img2Text.text = ligmage.images[1];
                    img3Text.text = ligmage.images[2];
                }
            }

            RowLayout {
                spacing: 10

                ColumnLayout {
                    Image {
                        id: img1
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        sourceSize.height: parent.height // Maintain aspect ratio
                        asynchronous: true
                        Layout.preferredHeight: parent.height / 3 // Set a preferred height
                        fillMode: Image.PreserveAspectFit
                    }

                    RowLayout {
                        Text {
                            id: img1Text
                            text: ""
                        }

                        Button {
                            text: "Copier"
                            onClicked: copyImageToClipboard(img1)

                            contentItem: Image {
                                source: Standard.icon(Standard.CopyIcon)
                            }
                        }

                    }
                }

                ColumnLayout {
                    Image {
                        id: img2
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        sourceSize.height: parent.height // Maintain aspect ratio
                        asynchronous: true
                        Layout.preferredHeight: parent.height / 3 // Set a preferred height
                        fillMode: Image.PreserveAspectFit
                    }

                    RowLayout {
                        Text {
                            id: img2Text
                            text: ""
                        }

                        Button {
                            text: "Copier"
                            onClicked: copyImageToClipboard(img2)

                            contentItem: Image {
                                source: Standard.icon(Standard.CopyIcon)
                            }
                        }

                    }
                }

                ColumnLayout {
                    Image {
                        id: img3
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        sourceSize.height: parent.height // Maintain aspect ratio
                        asynchronous: true
                        Layout.preferredHeight: parent.height / 3 // Set a preferred height
                        fillMode: Image.PreserveAspectFit
                    }

                    RowLayout {
                        Text {
                            id: img3Text
                            text: ""
                        }

                        Button {
                            text: "Copier"
                            onClicked: copyImageToClipboard(img3)

                            contentItem: Image {
                                source: Standard.icon(Standard.CopyIcon)
                            }
                        }

                    }
                }
            }
        }
    }
}
