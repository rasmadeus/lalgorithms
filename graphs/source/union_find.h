#pragma once

#include <graphs_export.h>
#include <vector>

namespace lalg
{
    class GRAPHS_EXPORT QuickFind
    {
    public:
        QuickFind(std::size_t numberOfVertexes);
        bool connected(std::size_t vertex1, std::size_t vertex2) const;
        std::size_t parent(std::size_t vertex) const;
        void unionSet(std::size_t vertex1, std::size_t vertex2);
        std::size_t numberOfVertexes() const;
        void show() const;

    private:
        std::vector<std::size_t> m_vertexParents;
    };

    class GRAPHS_EXPORT QuickUnion
    {
    public:
        QuickUnion(std::size_t numberOfVertexes);
        bool connected(std::size_t vertex1, std::size_t vertex2) const;
        std::size_t parent(std::size_t vertex) const;
        void unionSet(std::size_t vertex1, std::size_t vertex2);
        std::size_t numberOfVertexes() const;

    private:
        std::vector<std::size_t> m_vertexParents;
    };
}