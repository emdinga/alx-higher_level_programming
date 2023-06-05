#include "lists.h"
/**
 * check_cycle - Main function to check the list
 * @list: Parameter value
 *
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
