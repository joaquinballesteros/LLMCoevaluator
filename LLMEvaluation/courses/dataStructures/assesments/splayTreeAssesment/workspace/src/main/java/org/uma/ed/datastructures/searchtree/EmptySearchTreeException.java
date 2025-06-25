package org.uma.ed.datastructures.searchtree;

import java.io.Serial;

/**
 * Exceptions for empty search trees.
 *
 * @author Pepe Gallardo, Data Structures, Grado en Informática. UMA.
 */
public class EmptySearchTreeException extends RuntimeException {
  @Serial
  private static final long serialVersionUID = 2682430661350355887L;

  public EmptySearchTreeException() {
    super();
  }

  public EmptySearchTreeException(String msg) {
    super(msg);
  }
}
