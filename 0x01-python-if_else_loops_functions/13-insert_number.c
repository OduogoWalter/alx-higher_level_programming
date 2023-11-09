#include "lists.h"
#include <stdlib.h>
#include <sttddef.h>

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: the address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *temp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	temp = NULL;

	while (current != NULL && current->n < number)
	{
		temp = current;
		current = current->next;
	}

	if (temp == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		temp->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
