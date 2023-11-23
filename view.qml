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
                    id: pathText
                    width: parent.width
                    wrapMode: Text.Wrap
                    elide: Text.ElideRight
                    text: "Dossier"
                }

            }

            // --

            Item {}
            Item {}
            Item {}

            // --

            RowLayout {
                Button {
                    id: ligmageButton
                    objectName: "ligmageButton"
                    text: qsTr("Lancer le traitement")
                    onClicked: backend.run_ligmage()
                }
            }

            Text {
                id: progressText
                text: "Statut : 0/0"
                font.family: "Helvetica"
                font.pointSize: 12
                color: "green"
                
                Component.onCompleted: {
                    ligmage.progress_changed.connect(updateProgressText)
                }

                function updateProgressText() {
                    progressText.text = "Statut : " + ligmage.progress.join("/")
                }
            }
            
        }
    }
}
