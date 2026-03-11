import type { GenerateRequest } from "../../types/generator"


interface Props {
    data: GenerateRequest;
}

function PreviewPanel({ data }: Props) {
    return (
        <div className="bg-gray-900 text-green-400 px-6 py-10 rounded text-sm overflow-auto">
            <pre>
                {JSON.stringify(data, null, 2)}
            </pre>
        </div>
    )
}

export default PreviewPanel