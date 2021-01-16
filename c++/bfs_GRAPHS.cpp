// g++ bfs_GRAPHS.cpp -o bfs
// ./bfs
#include <vector>
#include <stack>
#include <queue>
#include <sstream>
#include <iostream>

using namespace std;


// BASE CLASES FOR GRAPHS

class Adjacent {
public:
    int dest, weight;
    Adjacent(int dest, int weight) {
        this -> dest = dest;
        this -> weight = weight;
    }
};

class Graph {
public:
    int nodeNum, edgeNum;
    vector<int> inDeg; // input degree
    vector<vector<Adjacent>> adjacents;

    Graph(int nodeNum) {
       this -> nodeNum = nodeNum;
       this -> edgeNum = 0;

       inDeg.resize(nodeNum, 0);
       adjacents.resize(nodeNum); 
    }

    void insertEdge(int origin, int dest, int weight) {
        Adjacent adj(dest, weight);

        this -> adjacents[origin].push_back(adj);
        this -> inDeg[dest] ++;
        this -> edgeNum ++;
    }

    int getEdge(int origin, int dest) {
        for (auto adj: this -> adjacents[origin]) {
            if(adj.dest == dest)
                return adj.weight;
        } 
        return 0;
    }

    bool existsEdge(int origin, int dest) {
        for(auto adj: this -> adjacents[origin]){
            if(adj.dest == dest)
                return true;
        }
        return false;
    }

    void delEdge(int origin, int dest) {
        for(unsigned int i = 0; i < adjacents[origin].size(); i++){
            Adjacent adj = adjacents[origin][i];
            if(adj.dest == dest){
                adjacents[origin].erase(adjacents[origin].begin() + i);
                this -> inDeg[origin] --;
                this -> edgeNum --;
            }
        }
    }

    string toString() {
        stringstream res;
        for(unsigned int i = 0; i < nodeNum; i ++){
            res << "Vertex: " << i;

            vector<Adjacent> adj = adjacents[i];
            if(adj.empty()) {
                res << " without adjacents";
            } else {
                res << " with adjacents: ";
            }

            for(auto a: adj) {
                res << "-> " << a.dest << "(" << a.weight << ") ";
            }
            res <<"\n";
        }
        return res.str();
    }

    string toString(vector<int> l, string text = ""){
        stringstream res;
        res << text << " ";
        for(unsigned int i = 0; i < l.size(); i ++) {
            res << " -> " << l[i];
        }
        return res.str();
    }

    // BFS
    vector<int> BFS(int origin) {
        vector<bool> visited(adjacents.size(), false);
        vector<int> vOrder;
        queue<int> bfsq;

        bfsq.push(origin);
        visited[origin] = true;

        while(!bfsq.empty()) {
            int current = bfsq.front();
            bfsq.pop();
            vOrder.push_back(current);

            for(auto adj: adjacents[current]){
                if(!visited[adj.dest]){
                    bfsq.push(adj.dest);
                    visited[adj.dest] = true;
                }
            }
        }
        return vOrder;
    }
};




int main(){
    cout << "======================== GRAPH ========================" << endl<<endl;
    Graph g(9);
    g.insertEdge(0, 1, 0);  //AB
    g.insertEdge(1, 2, 0);  //BC
    g.insertEdge(1, 3, 0);  //BD
    g.insertEdge(1, 5, 0);  //BF
    g.insertEdge(2, 0, 0);  //CA
    g.insertEdge(3, 4, 0);  //DE
    g.insertEdge(4, 5, 0);  //EF
    g.insertEdge(5, 3, 0);  //FD
    g.insertEdge(4, 6, 0);  //EG
    g.insertEdge(6, 5, 0);  //GF
    g.insertEdge(5, 7, 0);  //FH
    g.insertEdge(7, 8, 0);  //HI
    g.insertEdge(8, 7, 0);  //IH
    cout << g.toString() << endl;
    cout << "=======================================================" << endl;
    cout << "BFS: "<< g.toString(g.BFS(0)) <<endl;
    
    return 0;
}