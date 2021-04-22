import QtQuick 2.0
import QtQuick.Controls 2.15

Item {
    Rectangle {
        id: rectangle
        color: "#2e324a"
        anchors.fill: parent

        Label {
            id: label
            color: "#8f9091"
            text: qsTr("Description")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 300
            anchors.leftMargin: 300
            anchors.topMargin: 50
            font.pointSize: 16
        }

        Rectangle {
            id: descriptionText
            color: "#1e2130"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: label.bottom
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 190
            anchors.rightMargin: 100
            anchors.leftMargin: 100
            anchors.topMargin: 10
            radius: 10

            Text {
                id: textForDescription
                color: "#8f9091"
                text: qsTr("\nThis software was made using Qt and Python. It is based on Google Cloud \nText-to-speech library.\n You can use the source code, but you have to configure your own Google Cloud key with API enabled ")
                anchors.fill: parent
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignTop

                Image {
                    id: image
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    source: "../../images/LOGO_ROUND.png"
                    anchors.rightMargin: 229
                    anchors.leftMargin: 229
                    anchors.bottomMargin: 0
                    anchors.topMargin: 60
                    fillMode: Image.PreserveAspectFit
                }
            }
        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:800}D{i:2}D{i:5}D{i:4}D{i:3}D{i:1}
}
##^##*/
