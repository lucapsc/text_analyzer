class TextAnalyzer:
    def __init__(self, text):
        self.default_text = text
        self.fmtText = text.lower().replace("-", " ").replace("/", " ").replace('.'," ").replace\
            ('!'," ").replace('?'," ").replace(','," ").replace(';'," ").replace("*"," ")
        self.words = self.fmtText.split()
        self.freq = {}
        for word in set(self.words):
            self.freq[word] = self.words.count(word)
    def word_freq(self, word):
        self.word = word.lower()
        if self.word in self.freq:
            print("The word","\""+str(word)+"\"","appears in the text",self.freq[self.word],"times.")
        else:
            print("The word","\""+str(word)+"\"","is not in the text.")
    def max_words(self):
        smaller = 0
        self.tie_list = []
        for word in self.freq:
            if self.freq[word] > smaller:
                self.tie_list = []
                smaller = self.freq[word]
                self.tie_list.append(word)
            elif self.freq[word] == smaller:
                self.tie_list.append(word)
        return (self.tie_list)
    def make_backwards(self):
        backwards = ""
        for i in reversed(self.default_text):
            backwards += i
        return backwards

with open("C:/Users/lucas/IdeaProjects/untitled1/Sample_Essay.txt", encoding="utf8") as File1:
    FileContent = File1.read()
FileAnalyzed = TextAnalyzer(FileContent)
print(str(FileAnalyzed.freq[FileAnalyzed.max_words()[0]]) + ": ", FileAnalyzed.max_words())
while len(FileAnalyzed.freq) > 0:
    for word in FileAnalyzed.max_words():
        FileAnalyzed.freq.pop(word)
    try:
        print(str(FileAnalyzed.freq[FileAnalyzed.max_words()[0]]) + ": ", FileAnalyzed.max_words())
    except(IndexError):
        break
