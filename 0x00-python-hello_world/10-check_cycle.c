#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function to check singly linked list for cycle
 * @list: Head of list to be investigated
 * Return: 0 if no cycle 1 if theres a cycle
 */

int check_cycle(listint_t *list)
{
	node *traversed_head = NULL;

	while (list != NULL)
	{
		/* it isnt NULL, lets check if it already existsm*/
		if (check_list(list, traversed_head) == 1)
		{
			free_nodes(traversed_head);
			return (1);
		}
		/* no match in the list, then we record the address of the node */
		/* and create a new node */
		addnode(&traversed_head, list);
		list = list->next;
	}
	/* if while loop completes without a return, then no cycle */
	free_nodes(traversed_head);
	return (0);
}

/**
 * check_list - check if a node has been visited twice
 * @verify: address of current node being investigated
 * @against: Head of list used to store addresses of traversed nodes
 * Return: 0 if no match, 1 if there is a match
 */

int check_list(listint_t *verify, node *against)
{
	if (against != NULL) /* handle empty list supplied */
	{
		while (verify != against->traversed_node_add)
		{
			if (against->next == NULL)
				return (0);
			against = against->next;
		}
		return (1);
	}
	return (0);
}

/**
 * addnode - create a new node to hold the address of node being investigated
 * @head: pointer variable to hold address of the Head of storage linked list
 * @focus_node: node's address to be stored in storage list
 * Return: 0 on success, -1 on failure
 */

int addnode(node **head, listint_t *focus_node)
{
	/* make sure we're at the last node */
	while (*head != NULL)
		head = &((*head)->next);
	*head = malloc(sizeof(node));
	if (*head == NULL)
	{
		return (-1);
	}
	(*head)->traversed_node_add = focus_node;
	(*head)->next = NULL;
	return (0);
}
/**
 * free_nodes - free dynamically allocatted memory
 * @head: head of list whose nodes are to be freed
 */

void free_nodes(node *head)
{
	node *temp;

	while (head != NULL)
	{
		temp = head->next;
		free(head);
		head = temp;
	}
}

