class Solution:
    def is_palindrome_check(self, s: str) -> bool:
        s = [c.lower() for c in s]
        check_list = list(range(48, 58)) + list(range(97, 123))

        answer = [c for c in s
                  for check in check_list if c == chr(check)]

        if len(answer) == 0:
            return print("true")
        else:
            string_total_len = len(answer)

        ans = 0
        if string_total_len % 2 == 0:
            string_len = string_total_len // 2
            string_total_len -= 1
            for i in range(string_len):
                if answer[i] != answer[string_total_len]:
                    ans = 0
                    break
                ans += 1
                string_total_len -= 1
        elif string_total_len % 2 == 1:
            string_len = (string_total_len // 2)
            string_total_len -= 1
            string_mid = answer[string_len]
            idx = 0
            while idx < string_len:
                if answer[idx] != answer[string_total_len]:
                    ans = 0
                    break
                idx += 1
                ans += 1
                string_total_len -= 1

        if ans > 0:
            return print("True")
        elif ans == 0:
            return print("False")


# string = list(map(str, input()))
string = input()
palindrome = Solution()
palindrome.is_palindrome_check(string)
