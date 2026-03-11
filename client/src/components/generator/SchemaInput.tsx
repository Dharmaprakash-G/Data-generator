
interface Props {
    value: string;
    onChange: (value: string) => void;
}

function SchemaInput({ value, onChange }: Props) {
    return (
        <div className='mb-8'>
            <h2 className='text-xl font-semibold mb-3'>
                Database Schema
            </h2>

            <textarea
                placeholder='Paste your SQL schema here'
                rows={8}
                value={value}
                onChange={(e) => onChange(e.target.value)}
                className='w-full border border-gray-300 rounded-lg p-4 focus:outline-none focus:ring-blue-500'
            />
        </div>
    )
}

export default SchemaInput