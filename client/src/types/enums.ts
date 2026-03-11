export const COLUMN_TYPES = [
    "int",
    "full_name",
    "first_name",
    "last_name",
    "email",
    "user_name",
    "phone",
    "address",
    "city",
    "country",
    "zip_code",
    "url",
    "company",
    "text",
    "paragraph",
    "date",
    "uuid",
    "boolean",
] as const;

export type ColumnType = typeof COLUMN_TYPES[number];