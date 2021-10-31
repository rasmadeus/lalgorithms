#include "union_find_test.h"

namespace lalg
{
    TEST_F(UnionFindTest, TestDefaultObject)
    {
        EXPECT_EQ(10, m_unionFind.numberOfVertexes());

        for (std::size_t i = 0; i < m_unionFind.numberOfVertexes(); ++i) {
            EXPECT_EQ(i, m_unionFind.parent(i));
        }
    }

    TEST_F(UnionFindTest, TestUnion)
    {
        m_unionFind.unionSet(1, 2);
        m_unionFind.unionSet(1, 3);
        EXPECT_TRUE(m_unionFind.connected(2, 3));
        EXPECT_EQ(1, m_unionFind.parent(2));
        EXPECT_EQ(1, m_unionFind.parent(3));

        m_unionFind.unionSet(3, 4);
        EXPECT_TRUE(m_unionFind.connected(3, 4));
        EXPECT_EQ(1, m_unionFind.parent(4));
    }
}
