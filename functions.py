from double_ll import DoubleLinkedList


class Functions:
    def __init__(self, lst):
        self.lst = lst

    def every_second_node(self, counter=0):
        self.counter = 1
        current_node = self.lst.get_head_node()

        while current_node:
            if current_node.get_value() != None and self.counter % 2 == 0:
                print(current_node.get_value())
            current_node = current_node.get_link()
            self.counter += 1

    def get_length(self, lst):
        self.length = 0
        current_node = lst.get_head_node()

        while current_node:
            if current_node.get_value() != None:
                self.length += 1
            current_node = current_node.get_link()
        
        return self.length
        

    def remove_middle(self, lst):
        counter = 1
        current_node = lst.get_head_node()
        
        middle_index = self.get_length(lst) // 2
        while current_node:
            if current_node.get_value() != None:
                if counter == middle_index:
                    current_node_next_node = current_node.get_link()
                    current_node_prev_node = current_node.get_prev_link()

                    current_node_next_node.set_prev_link(current_node_prev_node)
                    current_node_prev_node.set_link(current_node_next_node)
                    print(lst.stringify_list())
                    break
            
            current_node = current_node.get_link()
            counter += 1

    def remove_by_value_reverse(self, value):
        node_to_remove = None 
        current_node = lst.tail_node
        
        while current_node:
            if current_node.get_value() == value:
                node_to_remove = current_node 
                break 
            current_node = current_node.get_prev_link()
            print(current_node.get_value())
        
        if node_to_remove == None:
            return None
        elif node_to_remove == lst.head_node:
            lst.remove_head()
        elif node_to_remove == lst.tail_node:
            lst.remove_tail()
        else:
            next_node = node_to_remove.get_link()
            prev_node = node_to_remove.get_prev_link()

            next_node.set_prev_link(prev_node)
            prev_node.set_link(next_node)
        
        return node_to_remove
        


        

''' Test Inputs 
lst = DoubleLinkedList()

lst.add_to_head(2)
lst.add_to_head(1)
lst.add_to_tail(3)
lst.add_to_tail(4)

functions = Functions(lst)

print(functions.remove_by_value_reverse(2))
'''