class HashMap:
    def __init__(self, capacity=20):
        # Create a list of empty buckets with the specified initial capacity.
        self.list = [[] for _ in range(capacity)]

    def insert(self, key, value):
        # Calculate the bucket where the key-value pair should be inserted.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Check if the key already exists in the bucket. If it does, update the value.
        for pair in bucket_list:
            if pair[0] == key:
                pair[1] = value
                return True

        # If the key doesn't exist, append the key-value pair to the bucket.
        bucket_list.append([key, value])
        return True

    # Time complexity: O(1) average case
    # Time complexity: O(n) worst case

    def get(self, key):
        # Calculate the bucket where the key-value pair should be located.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Search the bucket for the specified key and return the corresponding value.
        for pair in bucket_list:
            if pair[0] == key:
                return pair[1]

        # If the key is not found, return None.
        return None

    # Time complexity: O(1) average case
    # Time complexity: O(n) worst case

    def remove(self, key):
        # Calculate the bucket where the key-value pair should be inserted.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Iterate over the key-value pairs in the bucket and delete the pair if the key matches.
        for (i, k) in (bucket_list):
            if k == key:
                del bucket_list[i]
                break

    # Time complexity: O(n) average case
    # Time complexity: O(n) worst case
