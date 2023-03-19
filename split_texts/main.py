from src.text_splitter import TextSplitter
from src.mean_sent_len_counter import MeanSentLenCounter


if __name__ == '__main__':
    sent_len_counter = MeanSentLenCounter()
    sent_len_counter.count_mean_sent_len()
    TextSplitter().split(sent_len_counter.get_mean_len())
