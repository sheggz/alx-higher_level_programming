/*
 * EDGE CASES
 * what if we're givien an empty list i.e NULL
 * if we're to store negative numbers?
 * what about floats
 */

#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - a function that inserts a node in a sorted singly linked list
 * @head: a varable that stores the address of the HEAD pointer variable
 * @number: the number to be stored in the new node to be inserted
 *
 * Return: a pointer to the new node or NULL on failure.
 *
 * DESCRIPTION:
 * this task tests ones strength with pointers. note that; listint_t **head,
 * will hold the address of the address of the pointer variable that stores the
 * address of the first node.ie the (listint_t *HEAD) from main which tracks d
 * start of the linked list by storing the address of the first no.
 *
 * NOTE THAT: the address stored in that HEAD must not be changed to another,
 * else we loose track of the begining of d linked list. bt since head = &HEAD
 * the *head will alter the value stored in that HEAD pointer variable, so WE
 * MUST AVOID THIS.
 *
 * WE can only derefernce 'head' i.e (*head) and assign it to something else
 * after 'head' (a pointerr to pointer) has been changed to store the address
 * of another variable of type (listint_t *) other than HEAD.
 * THE ONLY EXCEPTION IS WHEN WE'RE INSERTING A NODE BEFORE the "existing 1st"
 * NODE, such that thew node becomes the first node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (*head != NULL)
	{
		if (number < (*head)->n)
		{
			temp = *head;
			*head = new;
			new->next = temp;
			return (*head);
		}
		head = &((*head)->next);/*
					* this way we're not changing the value
					* of the actual HEAD pointer in d main
					*/
	}
	*head = new;
}
