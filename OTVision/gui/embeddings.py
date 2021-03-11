import PySimpleGUI as sg


class OTGuiElement:
    """Parent class for all own custom PySimpleGui elements within OpenTrafficCam"""

    # ? maybe class OTGuiElement(sg.Frame) ?
    def __init__(self, title="Empty Frame"):
        self.title = title
        self.layout = [[sg.Text("Empty Layout")]]
        self.pad = (0, 0)
        self.create_frame()

    def create_frame(self):
        print("Frame is created from layout")
        self.frame = sg.Frame(title=self.title, layout=self.layout, pad=self.pad)

    def create_window(self):
        print("Window for OTGuiElement is created from layout")
        # Create the window
        self.window = sg.Window(title=self.title, layout=self.layout)
        # Enter event loop
        while True:
            event, values = self.window.read()
            # Window-related events
            if event == sg.WINDOW_CLOSED or event == "Quit":
                break
            # OTGuiElement related events
            self.events(event=event, values=values)
        # Close window
        self.window.close()

    def events(self, event, values):
        print("Event:" + str(event))
        print("Values:" + str(values))


class FoldersAndFiles(OTGuiElement):
    def __init__(self, title):
        super().__init__(title=title)
    # TODO


class VideoPlayer(OTGuiElement):
    """Creates a video player object. After creating a new instance with
    <instance> = VideoPlayer() use "<instance>.frame" to embed instance of VideoPlayer
    in the layout of your window and "<instance>.events" to interact with VideoPlayer
    instance from the event loop of your window.

    Args:
        OTGuiElement (class): Parent class for all own custom PySimpleGui elements
        within OpenTrafficCam
    """

    def __init__(
        self, title="Video Player", video=None, shapes=None, drawing_mode=None
    ):
        super().__init__(title=title)
        self.create_layout()
        self.shapes = shapes

    def create_layout(self):
        self.width = 100
        self.height = self.width / 3 * 4
        self.graph_vidframe = sg.Graph(
            (self.height, self.width),
            (0, self.width),
            (self.height, 0),
            key="graph_vidframe",
            enable_events=True,
            drag_submits=True,
        )
        self.button_play = sg.B(
            "Play", size=(int(self.width * 0.49), 1), key="button_play"
        )
        self.button_pause = sg.B(
            "Pause", size=(int(self.width * 0.49), 1), key="button_pause"
        )
        self.slider_vidframe = sg.Slider(
            orientation="h", size=(self.width, 10), key="slider_vidframe"
        )
        self.layout = [
            [sg.Text("slider_size")],
            [self.graph_vidframe],
            [self.button_play, self.button_pause],
            [self.slider_vidframe],
        ]

    def events(self, event, values, shapes=None, shape_mode=None):
        print("Hi from inside video player event loop!")
        self.vidframe_no = self._get_vidframe_no(event, values)

    def _get_vidframe_no(self, event, values):
        pass

    def _retrieve_vidframe(self):
        pass

    def _draw_shapes(self):
        pass

    def _show_vidframe(self):
        pass

    def video_from_shapes(self):
        print("Get video path from shapes dict or shapes path")

    def shapes_from_video(self):
        print("Get shapes path from video path")


if __name__ == "__main__":
    video_player = VideoPlayer(title="My first video player")
    video_player.create_window()
