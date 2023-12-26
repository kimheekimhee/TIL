package org.Tree;

import java.util.*;

public class Tree<T> {

    private Node<T> root;

    public Tree(T rootData) {
        root = new Node<T>();
        root.data = rootData;
        root.children = new ArrayList<Node<T>>();
    }

    public static class Node<T> {
        private T data;
        private Node<T> parent;
        private List<Node<T>> children;
    }

    // DFS를 사용하여 트리 출력
    public void printTree() {
        printSubtree(root, "");
    }

    private void printSubtree(Node<T> node, String prefix) {
        if (node == null) {
            return;
        }
        System.out.println(prefix + node.data);
        for (Node<T> child : node.children) {
            printSubtree(child, prefix + "  ");
        }
    }

    // 트리에 노드를 추가하는 메소드 (옵션)
    public Node<T> addChild(Node<T> parent, T childData) {
        Node<T> childNode = new Node<T>();
        childNode.data = childData;
        childNode.parent = parent;
        childNode.children = new ArrayList<Node<T>>();
        parent.children.add(childNode);
        return childNode;
    }

    public static void main(String[] args) {
        Tree<String> tree = new Tree<>("root");
        Tree.Node<String> nodeA = tree.addChild(tree.root, "A");
        Tree.Node<String> nodeB = tree.addChild(tree.root, "B");
        tree.addChild(nodeA, "A1");
        tree.addChild(nodeA, "A2");
        tree.addChild(nodeB, "B1");

        tree.printTree();
    }
}
