#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cstddef>

bool is_invalid(long n)
{
    char s[32];
    char *first, *second;
    size_t nbytes;

    snprintf(s, 32, "%li", n);

    nbytes = strlen(s);
    if (nbytes % 2 != 0)
        return false;

    nbytes >>= 1;
    first = s;
    second = s + nbytes;

    if (!strncmp(first, second, nbytes)) {
        return true;
    }

    return false;
}

int main()
{
    FILE *stream;
    char *line {nullptr};
    size_t size {0};
    ssize_t nread;
    int j;
    char *str1, *str2;
    char *saveptr1, *saveptr2;
    char *token;
    char *subtoken;
    long total_invalid {0};

    stream = fopen("../input", "r");
    if (stream == NULL) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    while ((nread = getline(&line, &size, stream)) != -1) {
        printf("Retrieved line of length %zd:\n", nread);
        fwrite(line, nread, 1, stdout);
        puts("\n");

        char *range;
        for (j = 1, str1 = line; ; j++, str1 = NULL) {
            token = strtok_r(str1, ",", &saveptr1);
            if (token == NULL)
                break;
            printf("%d: %s\n", j, token);

            long start, end;
            subtoken = strtok_r(token, "-", &saveptr2);
            start = atol(subtoken);
            subtoken = strtok_r(NULL, "-", &saveptr2);
            end = atol(subtoken);

            long i;
            for (i = start; i <= end; i++)
            {
                if (is_invalid(i)) {
                    printf("\tinvalid ID: %li\n", i);
                    total_invalid += i;
                }
            }
        }
    }

    printf("Total invalid: %li\n", total_invalid);

    free(line);
    fclose(stream);
    exit(EXIT_SUCCESS);
}
