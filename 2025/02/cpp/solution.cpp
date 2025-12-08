#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cstddef>

bool is_invalid(long n)
{
    char s[32];
    char *first, *second;
    size_t nbytes;

    nbytes = snprintf(s, 32, "%li", n);

    if (nbytes % 2 != 0)
        return false;

    nbytes /= 2;
    first = s;
    second = s + nbytes;

    if (!strncmp(first, second, nbytes)) {
        return true;
    }

    return false;
}

bool is_invalid2(long n)
{
    char s[32];
    char check[32];
    size_t nbytes;
    int i, j;

    nbytes = snprintf(s, 32, "%li", n);

    for (i = 1; i <= nbytes / 2; i++) {
        if (nbytes % i == 0) {
            int nchunks = nbytes / i;
            memset(check, 0, 32);
            for (j = 0; j < nchunks; j++) {
                strncat(check, s, i);
            }
            if (!strncmp(s, check, nbytes))
                return true;
        }
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
    long total_invalid2 {0};

    stream = fopen("../input", "r");
    if (stream == NULL) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    while ((nread = getline(&line, &size, stream)) != -1) {
        char *range;
        for (j = 1, str1 = line; ; j++, str1 = NULL) {
            token = strtok_r(str1, ",", &saveptr1);
            if (token == NULL)
                break;

            long start, end;
            subtoken = strtok_r(token, "-", &saveptr2);
            start = atol(subtoken);
            subtoken = strtok_r(NULL, "-", &saveptr2);
            end = atol(subtoken);

            long i;
            for (i = start; i <= end; i++)
            {
                if (is_invalid(i)) {
                    total_invalid += i;
                }
                if (is_invalid(i) || is_invalid2(i)) {
                    total_invalid2 += i;
                }
            }
        }
    }

    printf("Total invalid: %li\n", total_invalid);
    printf("Total invalid 2: %li\n", total_invalid2);

    free(line);
    fclose(stream);
    exit(EXIT_SUCCESS);
}
