import cv2


class ExtractChessBoard(object):
    def __init__(self, image_path, show_process=True) -> None:
        self.show_process = show_process
        self._load_image(image_path)
        self._load_board_template()
        self.extract_board_alternative()

    def _load_image(self, path):
        self.screenshot = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if self.screenshot is None:
            raise FileNotFoundError("Image not found")

    def _load_board_template(self):
        self.template = cv2.imread(
            "board_template/board_template.png", cv2.IMREAD_GRAYSCALE
        )
        if self.template is None:
            raise FileNotFoundError("Template not found")

    def extract_board(self):
        ret, thresholded_screenshot = cv2.threshold(
            self.screenshot, 120, 255, cv2.THRESH_BINARY
        )

        ret, thresholded_template = cv2.threshold(
            self.template, 120, 255, cv2.THRESH_BINARY
        )

        if self.show_process:
            # display the thresholded screenshot
            cv2.imshow("thresholded screenshot", thresholded_screenshot)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            cv2.imshow("thresholded template", thresholded_template)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        res = cv2.matchTemplate(
            thresholded_screenshot, thresholded_template, cv2.TM_CCOEFF_NORMED
        )
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        w, h = self.template.shape[::-1]
        top_left = max_loc

        # Draw rectangle around the chessboard (optional)
        end_right = top_left[0] + w
        end_bottom = top_left[1] + h
        cv2.rectangle(
            self.screenshot, top_left, (end_right, end_bottom), (0, 255, 0), 2
        )

        # # cut board out of screenshot
        # self.board_cut = self.screenshot[
        #     top_left[1] : bottom_right[1], top_left[0] : bottom_right[0]
        # ]

        # display the screenshot with rectangle
        cv2.imshow("screenshot", self.screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return self.board_cut

    def extract_board_alternative(self):
        # thresholded_screenshot = cv2.adaptiveThreshold(
        #     self.screenshot,
        #     255,
        #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #     cv2.THRESH_BINARY,
        #     11,
        #     2,
        # )

        # if self.show_process:
        #     cv2.imshow("thresholded screenshot", thresholded_screenshot)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()

        ret, corners = cv2.findChessboardCorners(self.screenshot, (8, 8), None)
        if ret:
            cv2.drawChessboardCorners(self.screenshot, (8, 8), corners, ret)
            cv2.imshow("screenshot", self.screenshot)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Chessboard not found")
            return None
