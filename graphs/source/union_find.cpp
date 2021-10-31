#include "union_find.h"
#include <cassert>
#include <iostream>

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

    void UnionFind::unionSet(std::size_t vertex1, std::size_t vertex2)
    {
        assert(vertex1 < m_vertexParents.size());
        assert(vertex2 < m_vertexParents.size());

        auto const parent1 = parent(vertex1);
        auto const parent2 = parent(vertex2);

        if (parent1 == parent2) {
            return;
        }

        for (std::size_t i = 0; i < m_vertexParents.size(); ++i) {
            if (m_vertexParents[i] == parent2) {
                m_vertexParents[i] = parent1;
            }
        }
    }

    std::size_t UnionFind::numberOfVertexes() const
    {
        return m_vertexParents.size();
    }
    void UnionFind::show() const
    {
        for (std::size_t i = 0; i < m_vertexParents.size(); ++i) {
            std::cout << i << ":" << m_vertexParents[i] << ";";
            if (i < m_vertexParents.size() - 1) {
                std::cout << " ";
            }
        }
        std::cout << "\n";
    }
}
