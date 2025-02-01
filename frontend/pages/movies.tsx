import { useEffect, useState } from 'react';
import { api } from '../lib/api';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Movie } from '../lib/types';

export default function MoviesPage() {
  const [movies, setMovies] = useState<Movie[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
    
  useEffect(() => {
    async function loadMovies() {
      try {
        const data = await api.getNewMovies(1990, 7.0);
        setMovies(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to fetch movies');
      } finally {
        setLoading(false);
      }
    }

    loadMovies();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <main className="container mx-auto py-10 space-y-8">
      <div className="flex flex-col gap-4">
        <h1 className="text-4xl font-bold tracking-tight">Popular Movies</h1>
        <p className="text-muted-foreground">
          Discover movies released since 1990
        </p>
      </div>

      <div className="rounded-lg border bg-card text-card-foreground shadow">
        <div className="relative w-full overflow-auto">
          <Table>
            <TableHeader>
              <TableRow className="hover:bg-transparent">
                <TableHead className="font-semibold">Title</TableHead>
                <TableHead className="font-semibold">Released</TableHead>
                <TableHead className="font-semibold">Rating</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {movies.map((movie) => (
                <TableRow key={movie.movieId} className="hover:bg-muted/50">
                  <TableCell className="font-medium">{movie.title}</TableCell>
                  <TableCell>{movie.released}</TableCell>
                  <TableCell>
                    <span className="inline-flex items-center rounded-md bg-yellow-50 px-2 py-1 text-xs font-medium text-yellow-800 ring-1 ring-inset ring-yellow-600/20">
                      ★ {movie.rating}
                    </span>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </div>
    </main>
  );
}
