class MyLinkedList {
    struct Node {
        int val;
        Node* next;
        Node(int x = 0, Node* n = nullptr): val(x), next(n) {}
    };
    
    Node* head;
    int size;
public:
    MyLinkedList() {
        head = new Node();
        size = 0;
    }
    
    int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        Node* itr = head->next;
        while(index > 0) {
            itr = itr -> next;
            index--;
        }
        return itr->val;
    }
    
    void addAtHead(int val) {
        Node* p = head -> next;
        head -> next = new Node(val, p);
        size++;
    }
    
    void addAtTail(int val) {
        Node* itr = head;
        while (itr -> next != nullptr) {
            itr = itr -> next;
        }
        itr -> next = new Node(val);
        size++;
    }
    
    void addAtIndex(int index, int val) {
        if (index < 0 || index > size) {
            return;
        }
        Node* itr = head;
        while(index > 0) {
            index--;
            itr = itr -> next;
        }
        itr->next = new Node(val, itr -> next);
        size++;
    }
    
    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        Node* itr = head;
        while(index > 0) {
            index--;
            itr = itr -> next;
        }
        Node* p = itr -> next;
        itr -> next = p -> next;
        delete p;
        size--;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */