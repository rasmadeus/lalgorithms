#include "union_find_test.h"

namespace lalg
{
    TEST_F(UnionFindTest, TestDefaultObject)
    {
        EXPECT_EQ(10, m_quickFind.numberOfVertexes());
        EXPECT_EQ(10, m_quickUnion.numberOfVertexes());

        for (std::size_t i = 0; i < m_quickFind.numberOfVertexes(); ++i) {
            EXPECT_EQ(i, m_quickFind.parent(i));
            EXPECT_EQ(i, m_quickUnion.parent(i));
        }
    }

    TEST_F(UnionFindTest, TestUnion)
    {
        m_quickFind.unionSet(1, 2);
        m_quickFind.unionSet(1, 3);
        EXPECT_TRUE(m_quickFind.connected(2, 3));
        EXPECT_EQ(1, m_quickFind.parent(2));
        EXPECT_EQ(1, m_quickFind.parent(3));

        m_quickUnion.unionSet(1, 2);
        m_quickUnion.unionSet(1, 3);
        EXPECT_TRUE(m_quickUnion.connected(2, 3));
        EXPECT_EQ(1, m_quickUnion.parent(2));
        EXPECT_EQ(1, m_quickUnion.parent(3));

        m_quickFind.unionSet(3, 4);
        EXPECT_TRUE(m_quickFind.connected(3, 4));
        EXPECT_EQ(1, m_quickFind.parent(4));

        m_quickUnion.unionSet(3, 4);
        EXPECT_TRUE(m_quickUnion.connected(3, 4));
        EXPECT_EQ(1, m_quickUnion.parent(4));
    }
}
