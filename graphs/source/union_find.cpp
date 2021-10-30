#include "union_find.h"
#include <cassert>

namespace lalg
{
    UnionFind::UnionFind(std::size_t numberOfVertexes)
        : m_vertexParents(numberOfVertexes, 0)
    {
        for (std::size_t i = 0; i < m_vertexParents.size(); ++i) {
            m_vertexParents[i] = i;
        }
    }

    bool UnionFind::connected(std::size_t vertex1, std::size_t vertex2) const
    {
        assert(vertex1 < m_vertexParents.size());
        assert(vertex2 < m_vertexParents.size());
        return parent(vertex1) == parent(vertex2);
    }

    std::size_t UnionFind::parent(std::size_t vertex) const
    {
        assert(vertex < m_vertexParents.size());
        return m_vertexParents[vertex];
    }

    void UnionFind::unionSet(std::size_t child, std::size_t parent)
    {
        assert(child < m_vertexParents.size());
        assert(parent < m_vertexParents.size());

        for (std::size_t i = 0; i < m_vertexParents.size(); ++i) {
            if (m_vertexParents[i] == child) {
                m_vertexParents[i] = parent;
            }
        }
    }
}
