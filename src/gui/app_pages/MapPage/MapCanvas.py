from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QWheelEvent, QMouseEvent, QPainter, QPen, QColor
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsTextItem, \
    QGraphicsLineItem


class MapCanvas(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

        self._last_mouse_pos = None
        self.scale_factor = 100000  # 1 degree = 100,000 pixels (adjust as needed)

        # Reference point (GeoDEC center -> scene origin)
        self.center_lat = 45.81
        self.center_lon = 21.33

        # Graphics scene
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Draw example based on threshold coordinates
        self.draw_twys()
        self.draw_stands()
        self.draw_thresholds()

    def draw_stands(self):
        stands = [
            {"designator": "1", "position": [45.81097222222222, 21.319672222222223]},
            {"designator": "2", "position": [45.810849999999995, 21.32016388888889]},
            {"designator": "3", "position": [45.81068888888888, 21.320805555555555]},
            {"designator": "4", "position": [45.81046111111111, 21.321330555555555]},
            {"designator": "5", "position": [45.810091666666665, 21.3228]},
        ]

        radius = 20
        for stand in stands:
            lat, lon = stand["position"]
            pos = self.geo_to_scene(lat, lon)

            # Circle for the stand
            self.scene.addEllipse(pos.x() - radius, pos.y() - radius, radius * 2, radius * 2)

            # Text label near the circle
            label = QGraphicsTextItem(stand["designator"])
            label.setPos(pos.x() + radius + 2, pos.y() - radius)
            self.scene.addItem(label)

    def geo_to_scene(self, lat: float, lon: float) -> QPointF:
        """Map lat/lon to scene coordinates"""
        dx = (lon - self.center_lon) * self.scale_factor
        dy = -(lat - self.center_lat) * self.scale_factor  # Invert Y
        return QPointF(dx, dy)

    def draw_twys(self):
        twys = [
            [45.81482416042408,21.316683768702937, 45.81272313166926,21.315586362136678],
            [45.81272313166926,21.315586362136678, 45.81146073990012,21.320416628313712],
            [45.81146073990012,21.320416628313712,45.81368250490586,21.32159482191979],
            [45.81146073990012,21.320416628313712,45.81135970747351,21.320616904732642],
            [45.81135970747351,21.320616904732642, 45.81030877903638,21.324577593944483],
            [45.81030877903638,21.324577593944483, 45.81097542152778,21.32494303927272],
            [45.81097542152778,21.32494303927272, 45.80849734646244,21.335025220144214],
            [45.80849734646244,21.335025220144214, 45.80984239454999,21.33576339129746]
        ]

        for twy in twys:
            start_lat = twy[0]
            start_lon = twy[1]
            stop_lat = twy[2]
            stop_lon = twy[3]

            pt1 = self.geo_to_scene(start_lat, start_lon)
            pt2 = self.geo_to_scene(stop_lat, stop_lon)

            radius = 10
            line = QGraphicsLineItem(pt1.x(), pt1.y(), pt2.x(), pt2.y())
            pnn = QPen()
            pnn.setWidth(50)
            pnn.setColor(QColor.fromRgb(120, 120, 120))
            line.setPen(pnn)
            self.scene.addItem(line)

        for twy in twys:
            start_lat = twy[0]
            start_lon = twy[1]
            stop_lat = twy[2]
            stop_lon = twy[3]

            pt1 = self.geo_to_scene(start_lat, start_lon)
            pt2 = self.geo_to_scene(stop_lat, stop_lon)
            line = QGraphicsLineItem(pt1.x(), pt1.y(), pt2.x(), pt2.y())
            pnn = QPen()
            pnn.setWidth(3)
            pnn.setColor(QColor.fromRgb(250, 250, 0))
            line.setPen(pnn)
            self.scene.addItem(line)

    def draw_thresholds(self):
        # Example lat/lon pairs from GeoDEC
        threshold1 = [45.81527777777777, 21.316666666666666]
        threshold2 = [45.80444444444444, 21.359166666666667]

        pt1 = self.geo_to_scene(*threshold1)
        pt2 = self.geo_to_scene(*threshold2)

        # Draw circles at those points
        radius = 10
        # self.scene.addEllipse(pt1.x() - radius, pt1.y() - radius, radius * 2, radius * 2)
        # self.scene.addEllipse(pt2.x() - radius, pt2.y() - radius, radius * 2, radius * 2)

        # Draw a line between them (e.g. runway)
        line = QGraphicsLineItem(pt1.x(), pt1.y(), pt2.x(), pt2.y())
        pnn = QPen()
        pnn.setWidth(80)
        pnn.setColor(QColor.fromRgb(70,70,70))
        line.setPen(pnn)
        self.scene.addItem(line)

    def wheelEvent(self, event: QWheelEvent):
        """Zoom on scroll"""
        zoom_factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(zoom_factor, zoom_factor)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._last_mouse_pos = event.pos()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._last_mouse_pos:
            delta = event.pos() - self._last_mouse_pos
            self._last_mouse_pos = event.pos()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._last_mouse_pos = None
            self.setCursor(Qt.CursorShape.ArrowCursor)
        super().mouseReleaseEvent(event)
