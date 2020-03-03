# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
# For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-").
# We'll call such a concatenation, the transformation of a word.

# Return the number of different transformations among all words we have.

def uniqueMorseRepresentations(self, words: List[str]) -> int:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    result = set()

    for word in words:
        val = ""
        for letter in word:
            val += morse[ord(letter)-ord('a')]

        result.add(val)
    return len(result)