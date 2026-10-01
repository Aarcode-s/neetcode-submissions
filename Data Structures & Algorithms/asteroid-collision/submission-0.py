class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:


        stack = []

        for asteroid in asteroids:

            # Assume the current asteroid survives
            alive = True

            # Collision can happen only when:
            # stack top is moving RIGHT (+)
            # current asteroid is moving LEFT (-)
            while stack and asteroid < 0 and stack[-1] > 0:

                if stack[-1] < -asteroid:
                    # Stack asteroid is smaller -> it explodes
                    stack.pop()

                elif stack[-1] == -asteroid:
                    # Both are same size -> both explode
                    stack.pop()
                    alive = False
                    break

                else:
                    # Current asteroid is smaller -> it explodes
                    alive = False
                    break

            # If current asteroid survived all collisions
            if alive:
                stack.append(asteroid)

        return stack
           


