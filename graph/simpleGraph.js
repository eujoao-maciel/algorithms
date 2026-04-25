class Graph {
  constructor() {
    this.adjcencyList = {}
  }

  addVertex(vertex) {
    if (!this.adjcencyList[vertex]) {
      this.adjcencyList[vertex] = []
    }
  }

  addEdge(vertex1, vertex2) {
    this.adjcencyList[vertex1].push(vertex2)
    this.adjcencyList[vertex2].push(vertex1)
  }

  printGraph() {
    for (let vertex in this.adjcencyList) {
      console.log(vertex + " -> " + this.adjcencyList[vertex].join(", "))
    }
  }
}

const graph = new Graph()

graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")

graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("A", "D")
graph.addEdge("C", "D")

graph.printGraph()


