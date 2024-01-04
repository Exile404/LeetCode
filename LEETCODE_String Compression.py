class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        m_index = 0
        t_index = 0

        while t_index < len(chars):
            char = chars[t_index]
            count = 0

            while t_index < len(chars) and chars[t_index] == char:
                t_index += 1
                count += 1

            chars[m_index] = char
            m_index += 1

            if count > 1:
                for digit in str(count):
                    chars[m_index] = digit
                    m_index += 1

        return m_index