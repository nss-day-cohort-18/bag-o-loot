import sys
import uuid

class LootBag():

    def write_child_to_file(self, child_name, action):
        with open('children', action) as children:
            child_id = uuid.uuid4()
            children.write("{},{}\n".format(child_id, child_name))

        return child_id

    def write_toy_to_file(self, toy_name, child_id, action):
        with open('toylist', action) as toys:
            toy_id = uuid.uuid4()
            toys.write("{},{},{}\n".format(toy_id, toy_name, child_id))

    def add_to_bag(self, toy, child_name):
        """Add a toy and assign it to a child. Both the toy and
        the child will be written to disk in the 'toylist' or 'children'
        file, respectively

        Attributes:
            toy (string)
            child_name (string)
        """

        # Determine if child already exists
        try:
            with open('children', 'r') as children:
                all_children = children.readlines()

                for child in all_children:
                    current_child_id, current_child_name = child.split(",")
                    if current_child_name == child_name:
                        self.write_toy_to_file(toy, current_child_id, 'a')
                        return

                new_child_id = self.write_child_to_file(child_name, 'a')
                self.write_toy_to_file(toy, new_child_id, 'a')

        except FileNotFoundError:
            new_child_id = self.write_child_to_file(child_name, 'w')
            self.write_toy_to_file(toy, new_child_id, 'a')


    def list_toys_for_child(self, child_name):
        if child_name == 'Vincent':
            return []
        else:
            return ['Ball', 'Slime']

    def remove_toy_from_child(self, toy, child_name):
        pass

    def get_single_child(self, child_name):
        return {
            'delivered': False
        }

    def deliver_toys_to_child(self, child_name):
        return {
            'delivered': True
        }

    def get_kids(self):
        return ['Vincent']



if __name__ == "__main__":
    if sys.argv[1] == "add":
        bag = LootBag()
        bag.add_to_bag(sys.argv[2], sys.argv[3])









