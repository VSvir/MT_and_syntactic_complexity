import re
from pathlib import Path


class TextSplitter:
    def __init__(self, directory: str = 'texts'):
        self.texts_path = Path(directory)
        self.file_paths = tuple(self.texts_path.rglob('*.txt'))
        self.sentences = {'short': [], 'long': []}
        self.words_pattern = re.compile(r'\w+')

    def split(self, mean_value: float) -> None:
        for path in self.file_paths:
            with open(path, 'r', encoding='utf-8') as text_file:
                text_sents = tuple(text_file.readlines())
            for sent in text_sents:
                if len(self.words_pattern.findall(sent)) < mean_value:
                    self.sentences['short'].append(sent)
                else:
                    self.sentences['long'].append(sent)
            self._save(path.stem)
            self.sentences = {'short': [], 'long': []}

    def _save(self, file_name: str) -> None:
        for text_type, text in self.sentences.items():
            path = Path(self.texts_path / text_type)

            if not path.exists():
                path.mkdir(parents=True)

            with open(Path(path / f'{file_name}_{text_type}.txt'), 'w', encoding='utf-8') as save_file:
                save_file.write(''.join(text))
