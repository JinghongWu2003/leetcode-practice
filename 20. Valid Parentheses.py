class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        bucket = []

        for x in s:
            if x == "(" or x == "{" or x == "[":
                bucket.append(x)
            else:
                if bucket and x == ")" and bucket[-1] == "(":
                    bucket.pop()
                elif bucket and x == "]" and bucket[-1] == "[":
                    bucket.pop()
                elif bucket and x == "}" and bucket[-1] == "{":
                    bucket.pop()
                else:
                    return False

        return len(bucket) == 0

