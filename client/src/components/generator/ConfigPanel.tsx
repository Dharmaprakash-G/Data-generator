interface Props {
    records: number;
    format: "csv" | "sql" | "json";
    onRecordsChange: (value: number) => void;
    onFormatChange: (value: "csv" | "sql" | "json") => void;
}



function ConfigPanel({
    records,
    format,
    onRecordsChange,
    onFormatChange,
}: Props) {
    return (
        <div className="mb-8">
            <h2 className='text-xl font-semibold mb-4'>
                Configuration
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                {/*Records */}
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Records per table
                    </label>
                    <input
                        type="number"
                        className="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        value={records}
                        onChange={(e) => onRecordsChange(Number(e.target.value))}
                    />
                </div>

                {/* Output Format */}
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Output Format
                    </label>
                    <select
                        value={format}
                        onChange={(e) => onFormatChange(e.target.value as "csv" | "sql" | "json")}
                        className="border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
                        <option value='csv'>CSV</option>
                        <option value='sql'>SQL</option>
                        <option value='json'>JSON</option>
                    </select>
                </div>
            </div>
        </div>
    )
}

export default ConfigPanel