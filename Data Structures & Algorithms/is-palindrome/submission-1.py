class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char for char in s if char.isalnum())
        cleaned_text = cleaned_text.lower()
        reversed_text = cleaned_text[::-1]
        if reversed_text == cleaned_text:
            return True
        else:
            return False