import cv2

from utils.display_image import display_image


class ExtractChessBoard(object):
    def __init__(
        self, image_path="", image_obj=None, show_process=True, threshold_value=90
    ) -> None:
        self.show_process = show_process
        self.threshold_value = threshold_value
        self._load_image(image_path, image_obj)

    def _load_image(self, path, image_obj=None):
        if image_obj is not None:
            self.screenshot = image_obj
        else:
            self.screenshot = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if self.screenshot is None:
                raise FileNotFoundError("Image not found")

        self.original_image = self.screenshot

    def extract_board(self, extracted_board_size=(200, 200)):
        ret, thresholded_screenshot = cv2.threshold(
            self.screenshot, self.threshold_value, 255, cv2.THRESH_BINARY
        )

        if self.show_process:
            # display the thresholded screenshot
            cv2.imshow("thresholded screenshot", thresholded_screenshot)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        contours, hierarchy = cv2.findContours(
            thresholded_screenshot, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        biggest_area = 0
        biggest_cnt = None

        for cnt in contours:
            # Check if the contour is a rectangle (has 4 corners)
            if len(cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)) == 4:
                area = cv2.contourArea(cnt)
                if area > biggest_area:
                    biggest_area = area
                    biggest_cnt = cnt

        # Extract coordinates of the biggest rectangle (if found)
        if biggest_cnt is not None:
            x, y, w, h = cv2.boundingRect(biggest_cnt)
            cv2.rectangle(self.screenshot, (x, y), (x + w, y + h), (255, 255, 255), 2)

            if self.show_process:
                # display the screenshot with the rectangle
                cv2.imshow("screenshot with rectangle", self.original_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            # Extract the board from the screenshot
            self.board = self.screenshot[y : y + h, x : x + w]
            if self.show_process:
                # display the extracted board
                cv2.imshow("extracted board", self.board)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            self.board = cv2.threshold(
                self.board, self.threshold_value, 255, cv2.THRESH_BINARY
            )[1]

            if self.show_process:
                display_image(self.board, "thresholded extracted board")

            self.board = cv2.resize(self.board, extracted_board_size)
            return self.board
        else:
            raise Exception("No rectangle found")
