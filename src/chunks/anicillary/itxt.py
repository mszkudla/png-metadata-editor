from src.chunk import Chunk
from src.clear_terminal import clear_terminal


class ITXT(Chunk):
    def __init__(self, raw_chunk_bytes):
        super().__init__(raw_chunk_bytes)
        self.keyword = None
        self.compression_flag = None
        self.compression_method = None
        self.language_tag = None
        self.translated_keyword = None
        self.text = None
        self.analyse()

    def analyse(self):
        data = self.data
        data = data.split(b'\x00', 1)
        self.keyword = data[0].decode('utf-8')
        self.compression_flag = int.from_bytes(data[1][0:1], byteorder='big')
        self.compression_method = int.from_bytes(data[1][1:2], byteorder='big')
        data = data[1][2:]
        data = data.split(b'\x00', 1)
        self.language_tag = data[0].decode('iso-8859-1')
        data = data[1].split(b'\x00', 1)
        self.translated_keyword = data[0].decode('utf-8')
        self.text = data[1].decode('utf-8')

    def details(self):
        clear_terminal()
        self.print_basic_info()
        print('iTXT chunk info: ')
        print(' Keyword:', self.keyword)
        print(' Compression flag:', self.compression_flag)
        print(' Compression method:', self.compression_method)
        print(' Language tag:', self.language_tag)
        print(' Translated keyword:', self.translated_keyword)
        print(' Text:', self.text)
        print()
        