import QtQuick 2.1
import Sailfish.Silica 1.0
import org.nemomobile.configuration 1.0

Page {
    id: page

    ConfigurationGroup {
        id: toggles
        path: "/desktop/lipstick/sailfishos-patch-tabletui"
        property real portrait: 3
        property real landscape: 3
    }

    SilicaFlickable {
        id: flick
        anchors.fill: parent
        contentHeight: content.height

        Column {
            id: content
            width: parent.width
            spacing: Theme.paddingMedium

            PageHeader {
                title: "Tablet UI"
            }

            SectionHeader {
                text: qsTr("Portrait shortcuts")
            }

            Slider {
                id: sldportrait
                width: parent.width
//                label: qsTr("Portrait")
                maximumValue: 5
                minimumValue: 1
                stepSize: 1
                value: toggles.portrait
                valueText: value
                onPressAndHold: cancel()

                onReleased: {
                    toggles.portrait = value
                }
            }

            SectionHeader {
                text: qsTr("Landscape shortcuts")
            }

            Slider {
                id: sldlandscape
                width: parent.width
//                label: qsTr("Landscape")
                maximumValue: 5
                minimumValue: 1
                stepSize: 1
                value: toggles.landscape
                valueText: value
                onPressAndHold: cancel()

                onReleased: {
                    toggles.landscape = value
                }
            }

              SectionHeader { text: qsTr("Support") }

              Label {
                  x: Theme.paddingLarge
                  width: parent.width - (x * 2)
                  wrapMode: Text.Wrap
                  text: qsTr("If you like my work and want to buy me a beer, feel free to do it!")
              }

              Button {
                  anchors.horizontalCenter: parent.horizontalCenter
                  text: qsTr("Donate")
                  onClicked: Qt.openUrlExternally("https://www.paypal.me/fravaccaro")
              }

              SectionHeader { text: qsTr("Translations") }

              AboutLanguage { text: "Italiano" }
              AboutTranslator { text: "Francesco Vaccaro" }
              Item { width: parent.width; height: Theme.paddingLarge }

              Label {
                  x: Theme.paddingLarge
                  width: parent.width - (x * 2)
                  wrapMode: Text.Wrap
                  textFormat: Text.RichText
                  text: qsTr("Request a new language or contribute to existing languages on the Transifex project page.")
                  onLinkActivated: Qt.openUrlExternally(link)
              }

              Button {
                  anchors.horizontalCenter: parent.horizontalCenter
                  text: qsTr("Transifex")
                  onClicked: Qt.openUrlExternally("https://www.transifex.com/fravaccaro/tablet-ui-patch/")
              }

              Item { width: parent.width; height: Theme.paddingLarge }
        }

        VerticalScrollDecorator {
            flickable: flick
        }
    }
}
