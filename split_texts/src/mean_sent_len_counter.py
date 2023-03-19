import re
from pathlib import Path


class MeanSentLenCounter:
    def __init__(self, directory: str = 'texts'):
        self.file_paths = tuple(Path(directory).rglob('*.txt'))
        self.mean_sent_len = 0
        self.words_pattern = re.compile(r'\w+')

    def count_mean_sent_len(self) -> None:
        for path in self.file_paths:
            self.mean_sent_len += self._count_sent_len(path)
        self.mean_sent_len = round(self.mean_sent_len / len(self.file_paths), 2)

    def _count_sent_len(self, path: Path) -> float:
        with open(path, 'r', encoding='utf-8') as text_file:
            text = text_file.readlines()
        return round(len(self.words_pattern.findall(''.join(text))) / len(text), 2)

    def get_mean_len(self) -> float:
        return self.mean_sent_len
