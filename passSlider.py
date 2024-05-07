import cv2

class pass_slider():
    def __init__(self, puzzle, bg, left, top) -> None:
        self.puzzle_path = puzzle
        self.background_path = bg
        self.puzzle_left = left
        self.puzzle_top = top

    def _tran_canny(self, image):
        image = cv2.GaussianBlur(image, (3, 3), 0)
        return cv2.Canny(image, 50, 150)

    def show(self, name):
        cv2.imshow('Show', name)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def process(self) -> None:

        # flags0是灰度模式
        image = cv2.imread(self.background_path, 0)
        template = cv2.imread(self.puzzle_path, 0)
        template = cv2.resize(template, (680, 390), interpolation=cv2.INTER_CUBIC)

        # 寻找最佳匹配
        res = cv2.matchTemplate(self._tran_canny(image), self._tran_canny(template), cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        x, y = max_loc
        w, h = image.shape[::-1]
        cv2.rectangle(template, (x, y), (x + w, y + h), (7, 249, 151), 2)
        self.show(template)
        return min_loc, max_loc

def main():
    return 0

if __name__ == '__main__':
    left = 26 * 2
    top = 22 * 2
    start = (left, top)
    curInit = pass_slider("hycdn.jpg", "hycdn.png", left, top)
    puzzle_min, puzzle_max = curInit.process()
    print(tuple(puzzle_max[i] - start[i] for i in range(len(puzzle_max))))