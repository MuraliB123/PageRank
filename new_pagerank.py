from mrjob.job import MRJob
from mrjob.job import MRStep
from mrjob.protocol import JSONProtocol
import time,re, os, ntpath, math

 #PageRank Algorithm

class PageRank(MRJob):
    # def configure_args(self):
    #     super(PageRank,self).configure_args()

    #     self.add_passthru_arg('--graph_size',dest='graph_size',type=int, help='')
    
    INPUT_PROTOCOL = JSONProtocol
    def mapper(self, nid, node):
        # Unpack the values of the node
        adjacency_list, pagerank = node
        p = pagerank / len(adjacency_list)

        # Yield the node, labelled for the reducer
        yield nid, ('node', node)

        # Iterate through the adjacency list,
        for adj in adjacency_list:
            yield adj, ('pagerank', p)

    def reducer(self, nid, values):
        # Initialize sum and node
        cur_sum = 0
        node = ('node', [], cur_sum)

        for val in values:
            # Unpack the content of a value
            label, content = val

            # If it's a node, save the node
            if label == 'node':
                node = content
                previous_pagerank = content[1]

            # If it's a pagerank, store the pagerank
            # We will sum the pagerank values
            elif label == 'pagerank':
                cur_sum += content
                previous_pagerank = content
        cur_sum = 0.0214 + 0.85*cur_sum 
        # Bundle the adjacency list and the pagerank value
        node = (node[0], cur_sum)

        # Increment the unconverged node count (which is the number of updated nodes)
        

        # Return just the node
        yield nid, node
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(mapper=self.mapper,
                    reducer=self.reducer),
            MRStep(mapper=self.mapper,
                   reducer = self.reducer),
            MRStep(mapper = self.mapper,
                   reducer = self.reducer),
            MRStep(mapper = self.mapper,
                   reducer = self.reducer)
        ]               
if __name__ == '__main__':
    PageRank.run()


