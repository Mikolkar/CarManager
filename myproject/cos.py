import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsItem, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter

class MyGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()

        frame = QFrame(self)
        self.scene = QGraphicsScene(frame)
        self.setScene(self.scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        self.points = []

    def mousePressEvent(self, event):
        # Dodanie nowego punktu po kliknięciu myszą
        point = self.mapToScene(event.pos())
        item = QGraphicsEllipseItem(point.x() - 5, point.y() - 5, 10, 10)
        item.setBrush(Qt.GlobalColor.blue)
        item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.scene.addItem(item)
        self.points.append(item)

def main():
    app = QApplication(sys.argv)
    view = MyGraphicsView()
    view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
