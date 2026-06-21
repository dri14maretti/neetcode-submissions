public class Node 
{
    public int Key;
    public int Val;
    public Node Next;
    public Node Prev;

    public Node(int key, int val) {
        Key = key;
        Val = val;
    }
}

public class LRUCache 
{
    private Dictionary<int, Node> Cache;
    private Node Head;
    private Node Tail;
    private int Capacity;

    public LRUCache(int capacity) 
    {
        Cache = new Dictionary<int, Node>();
        Capacity = capacity;

        Head = new Node(0,0);
        Tail = new Node(0,0);
        Head.Next = Tail;
        Tail.Prev = Head;
    }
    
    public int Get(int key) 
    {
        if(Cache.Count == 0 || !Cache.ContainsKey(key))
            return -1;

        Node node = Cache[key];
        Remove(node);
        Insert(node);
        
        return Cache[key].Val;
    }
    
    public void Put(int key, int value) 
    {
        if(Cache.ContainsKey(key))
            Remove(Cache[key]);

        Node newNode = new Node(key, value);
        Cache[key] = newNode;
        Insert(newNode); 

        if (Cache.Count > Capacity) {
            Node lru = Head.Next;
            Remove(lru);
            Cache.Remove(lru.Key);
        }
    }

    private void Remove(Node node) {
        var next = node.Next;
        var previous = node.Prev;

        next.Prev = previous;
        previous.Next = next;
    }

    private void Insert(Node node) {
        var previous = Tail.Prev;
        previous.Next = node;
        node.Prev = previous;
        node.Next = Tail;
        Tail.Prev = node; 
    }
}
