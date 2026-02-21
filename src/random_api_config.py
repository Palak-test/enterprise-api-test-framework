import random

class RandomAPIConfig:
    @staticmethod
    def generate_config():
        return {
            "base_url": random.choice([
                "https://jsonplaceholder.typicode.com",
                "https://api.example.com",
                "https://api.test.com"
            ]),
            "timeout": random.randint(1, 10),
            "retries": random.randint(0, 5),
            "headers": {
                "Authorization": f"Bearer {random.randint(100000,999999)}",
                "Content-Type": random.choice(["application/json", "application/xml"])
            }
        }
