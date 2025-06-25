package org.uma.ed.datastructures.searchtree;

import java.util.Comparator;

/**
 * This interface represents a Search Tree, a data structure that stores unique keys in a sorted manner.
 * The sorting of keys is determined by the provided comparator or their natural order if no comparator is provided.
 * The uniqueness of keys is ensured by using the comparator for equality checks.
 *
 * @param <K> The type of keys in the search tree.
 *
 * @author Pepe Gallardo, Data Structures, Grado en Informática. UMA.
 */
public interface SearchTree<K> {
  /**
   * Returns the comparator used to define the order of keys in this search tree.
   *
   * @return The comparator used for key ordering.
   */
  Comparator<K> comparator();

  /**
   * Checks if the search tree is empty.
   *
   * @return {@code true} if the search tree contains no keys, {@code false} otherwise.
   */
  boolean isEmpty();

  /**
   * Returns the number of keys stored in the search tree.
   *
   * @return The number of keys in the search tree.
   */
  int size();

  /**
   * Returns the height of the search tree.
   *
   * @return The height of the search tree.
   */
  int height();

  /**
   * Inserts a new key into the search tree. If the key already exists, the existing key is replaced with the new key.
   * Duplicate keys are not supported.
   *
   * @param key The key to be inserted.
   */
  void insert(K key);

  /**
   * Searches for a key in the search tree and returns it if found. If the key is not found, returns {@code null}.
   *
   * @param key The key to search for.
   * @return The key from the search tree if found, {@code null} otherwise.
   */
  K search(K key);

  /**
   * Checks if a key is present in the search tree.
   *
   * @param key The key to check for.
   * @return {@code true} if the key is present in the search tree, {@code false} otherwise.
   */
  boolean contains(K key);

  /**
   * Removes a key from the search tree. If the key is not present, the search tree remains unchanged.
   *
   * @param key The key to be removed.
   */
  void delete(K key);

  /**
   * Removes all keys from the search tree, making it empty.
   */
  void clear();

  /**
   * Returns the smallest key in the search tree.
   *
   * @return The smallest key in the search tree.
   */
  K minimum();


  /**
   * Removes the smallest key from the search tree.
   */
  void deleteMinimum();



  /**
   * Returns an Iterable over all keys in the search tree in in-order traversal order.
   * The remove operation is not supported by the returned iterator.
   * The search tree structure or keys should not be modified during iteration.
   *
   * @return An Iterable over all keys in the search tree in in-order traversal order.
   */
  Iterable<K> inOrder();


}