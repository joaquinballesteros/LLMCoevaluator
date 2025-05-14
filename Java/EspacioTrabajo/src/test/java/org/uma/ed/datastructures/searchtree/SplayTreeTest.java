package org.uma.ed.datastructures.searchtree;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import static org.junit.jupiter.api.Assertions.*;


class SplayTreeTest {
        private SplayTree<Integer> tree;

        @BeforeEach
        void setUp() {
            tree = SplayTree.empty();
        }

        @Test
        void testInsert() {
            tree.insert(10);
            tree.insert(20);
            tree.insert(5);

            assertEquals(3,tree.size());

            Iterable<Integer> inOrder = tree.inOrder();
            Integer[] expected = {5, 10, 20};
            assertArrayEquals(expected, toArray(inOrder));

        }

        @Test
    void testInsertUpdate() {
            //Big number to avoid the Integer pool!
         Integer oldI = Integer.valueOf(1000);
        Integer newI = Integer.valueOf(1000);

        tree.insert(oldI);
        tree.insert(newI);

        assertEquals(1,tree.size());
        assertEquals(1000,tree.root.key);
        assertTrue(newI==tree.root.key);

    }

    @Test
    void cuandoUsasConstructorSinMensaje_elMensajeEsNull() {
        EmptySearchTreeException ex = new EmptySearchTreeException();
        // Por defecto RuntimeException.getMessage() devuelve null
        assertNull(ex.getMessage());
        // Tampoco debería tener causa
        assertNull(ex.getCause());
    }

    @Test
    void cuandoUsasConstructorConMensaje_elMensajeSeConserva() {
        String mensaje = "Árbol vacío";
        EmptySearchTreeException ex = new EmptySearchTreeException(mensaje);
        assertEquals(mensaje, ex.getMessage());
        assertNull(ex.getCause());
    }

    @Test
    void esUnchecked_esSubclaseDeRuntimeException() {
        EmptySearchTreeException ex = new EmptySearchTreeException();
        assertTrue(ex instanceof RuntimeException);
    }


        @Test
        void testSearch() {
            tree.insert(10);
            tree.insert(20);
            tree.insert(5);

            assertEquals(10, tree.search(10));
            assertEquals(10,tree.root.key);
            assertEquals(20, tree.search(20));
            assertEquals(20,tree.root.key);
            assertEquals(5, tree.search(5));
            assertEquals(5,tree.root.key);
            assertNull(tree.search(15));
        }

        @Test
        void testDelete() {
            tree.insert(10);
            tree.insert(20);
            tree.insert(5);

            tree.delete(10);
            Iterable<Integer> inOrder = tree.inOrder();
            Integer[] expected = {5, 20};
            assertArrayEquals(expected, toArray(inOrder));

            tree.delete(5);
            Integer[] expected1 = {5, 20};
            assertArrayEquals(expected1, toArray(inOrder));

            tree.delete(20);
            assertTrue(tree.isEmpty());
        }

        @Test
        void testMinimum() {
            tree.insert(10);
            tree.insert(20);
            tree.insert(5);

            assertEquals(5, tree.minimum());
        }


        @Test
        void testDeleteMinimum() {
            tree.insert(10);
            tree.insert(20);
            tree.insert(5);

            tree.deleteMinimum();
            assertFalse(tree.contains(5));
            assertEquals(10, tree.minimum());
            assertEquals(2,tree.size());
        }


        @Test
        void testClear() {
            tree.insert(10);
            tree.insert(20);
            tree.insert(5);

            tree.clear();
            assertTrue(tree.isEmpty());
        }

        @Test
        void testSize() {
            assertEquals(0, tree.size());

            tree.insert(10);
            assertEquals(1, tree.size());

            tree.insert(20);
            assertEquals(2, tree.size());

            tree.delete(10);
            assertEquals(1, tree.size());

            tree.clear();
            assertEquals(0, tree.size());
        }

        @Test
        void testHeight() {
            assertEquals(0, tree.height());

            tree.insert(10);
            assertEquals(1, tree.height());

            tree.insert(20);
            assertEquals(2, tree.height());

            tree.insert(5);
            System.out.println(tree.toString());

            tree.insert(10);
            assertEquals(2, tree.height());
        }

        @Test
        void testInOrder() {
            tree.insert(10);
            tree.insert(20);
            tree.insert(5);

            Iterable<Integer> inOrder = tree.inOrder();
            Integer[] expected = {5, 10, 20};
            assertArrayEquals(expected, toArray(inOrder));
        }

    @Test
    void testCopyOfSplay() {
        tree.insert(10);
        tree.insert(20);
        tree.insert(5);

        Iterable<Integer> inOrder1 = tree.inOrder();
        Iterable<Integer> inOrder2 = SplayTree.copyOf(tree).inOrder();

        assertArrayEquals(toArray(inOrder2), toArray(inOrder1));
    }

    @Test
    void testCopyOfSearchTree() {
        tree.insert(10);
        tree.insert(20);
        tree.insert(5);

        Iterable<Integer> inOrder1 = tree.inOrder();
        Iterable<Integer> inOrder2 = SplayTree.copyOf((SearchTree<Integer>)tree).inOrder();

        assertArrayEquals(toArray(inOrder2), toArray(inOrder1));
    }



        private Integer[] toArray(Iterable<Integer> iterable) {
            ArrayList<Integer> list = new ArrayList<>();
            for (Integer item : iterable) {
                list.add(item);
            }
            return list.toArray(new Integer[0]);
        }
}

