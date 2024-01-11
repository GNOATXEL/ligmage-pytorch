import QtCore
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs
import Qt.labs.platform
// import QtQuick.Controls.Material

Window {
    width: 720
    height: 480
    visible: true
    title: "Ligmage"
    // Material.theme: Material.Light

    FolderDialog {
        id: folderDialog
//        selectFolder: true
        title: qsTr("Dossier d'images")
        currentFolder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
        onAccepted: {
            pathText.text = "Dossier choisi : " + folder
            backend.file_url = folder
        }
    }

    RowLayout {
        anchors.fill: parent

        ColumnLayout {
            // id: mainGrid
            // columns: 3
            Layout.margins: 50
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
            // --
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

            // --

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

            // --

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
                }
            }

            Row {
                spacing: 10

                Image {
                    id: img1
                    width: 200
                    height: 200
                    sourceSize.width: parent.width // Maintain aspect ratio
                    anchors.verticalCenter: parent.verticalCenter
                    asynchronous: true
                }

                Image {
                    id: img2
                    width: 200
                    height: 200
                    sourceSize.width: parent.width // Maintain aspect ratio
                    anchors.verticalCenter: parent.verticalCenter
                    asynchronous: true
                }

                Image {
                    id: img3
                    width: 200
                    height: 200
                    sourceSize.width: parent.width // Maintain aspect ratio
                    anchors.verticalCenter: parent.verticalCenter
                    asynchronous: true
                }
            }
            
        }
    }
}
