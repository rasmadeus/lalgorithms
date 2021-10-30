#pragma once

#include <graphs_export.h>
#include <vector>

namespace lalg
{
    class GRAPHS_EXPORT UnionFind
    {
    public:
        UnionFind(std::size_t numberOfVertexes);
        bool connected(std::size_t vertex1, std::size_t vertex2) const;
        std::size_t parent(std::size_t vertex) const;
        void unionSet(std::size_t child, std::size_t parent);

    private:
        std::vector<std::size_t> m_vertexParents;
    };
}